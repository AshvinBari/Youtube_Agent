
import streamlit as st
from tavily import TavilyClient

from urllib.parse import urlparse, parse_qs

# -----------------------------------------
# Tavily initialization
# -----------------------------------------
TAVILY_API_KEY = "TAVILY_API_KEY"
client = TavilyClient(api_key=TAVILY_API_KEY)

st.set_page_config(page_title="AI YouTube Highest-View Video Finder", layout="wide")


# ------------------------------
# Extract video ID for thumbnail
# ------------------------------
def extract_youtube_id(url):
    parsed = urlparse(url)

    if parsed.hostname in ["www.youtube.com", "youtube.com"]:
        return parse_qs(parsed.query).get("v", [None])[0]

    if parsed.hostname == "youtu.be":
        return parsed.path[1:]

    return None


def get_thumbnail_url(video_url):
    video_id = extract_youtube_id(video_url)
    if video_id:
        return f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"
    return None


# ------------------------------
# Extract YouTube video results
# ------------------------------
def extract_youtube_results(results):
    videos = []

    for item in results:
        url = item.get("url", "")
        title = item.get("title", "")
        content = item.get("content", "")

        if "youtube.com/watch" in url or "youtu.be" in url:
            videos.append({
                "title": title,
                "url": url,
                "snippet": content[:300],
                "thumbnail": get_thumbnail_url(url)
            })

    return videos


# ------------------------------
# Highest View Video Selector
# ------------------------------
def pick_highest_view_video(videos):
    if not videos:
        return None

    keywords = ["views", "watched", "popular", "viral", "top", "trending"]

    def score(video):
        text = (video["title"] + " " + video["snippet"]).lower()
        return sum(text.count(k) for k in keywords)

    return sorted(videos, key=score, reverse=True)[0]


# ------------------------------
# Main Agent (NO GITHUB)
# ------------------------------
def youtube_agent(topic, level):
    level_map = {
        "Basic": "beginner easy tutorial step-by-step",
        "Intermediate": "intermediate practical project tutorial",
        "Advanced": "advanced expert-level deep dive tutorial"
    }

    query = (
        f"Highest viewed YouTube videos for learning {topic}. "
        f"Difficulty: {level_map[level]}. "
        "Return only YouTube videos."
    )

    result = client.search(query=query, max_results=12)

    youtube_links = extract_youtube_results(result["results"])
    best_video = pick_highest_view_video(youtube_links)

    return best_video, youtube_links


# ------------------------------
# Streamlit UI
# ------------------------------
st.title("🎥 AI Agent For YouTube")
st.write("Find the **best YouTube tutorial** for any topic using Tavily.")

topic = st.text_input("🔍 Enter Topic (e.g., Python Basics, Machine Learning, HTML Forms):")

levels = ["Basic", "Intermediate", "Advanced"]
level = st.selectbox("🎯 Choose Level", levels)

if st.button("Find Best Video"):
    if not topic.strip():
        st.error("Please enter a topic.")
    else:
        st.info("🔍 Searching the best YouTube tutorial...")

        best_video, all_videos = youtube_agent(topic, level)

        if not best_video:
            st.warning("No YouTube videos found. Try another topic.")
        else:
            st.subheader("🔥 Highest-View YouTube Recommendation")

            # Thumbnail
            if best_video["thumbnail"]:
                st.image(best_video["thumbnail"], width=450)

            st.markdown(f"### 🎬 {best_video['title']}")
            st.markdown(f"[▶ Watch Video]({best_video['url']})")
            st.write(best_video["snippet"])

            st.markdown("---")
            st.subheader("📌 Other Recommended Videos")

            for video in all_videos[1:]:
                if video["thumbnail"]:
                    st.image(video["thumbnail"], width=300)

                st.markdown(f"**{video['title']}**")
                st.markdown(f"[Open Link]({video['url']})")
                st.write(video["snippet"])
                st.markdown("---")
