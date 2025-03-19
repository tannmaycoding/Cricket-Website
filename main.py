import streamlit as st
import cricket
import tempfile
import os

st.title("Cricket")
st.markdown("## Upload the video here:")
video = st.file_uploader(label="Upload", type="mp4", accept_multiple_files=False)
colour = st.selectbox("Colour of ball", options=["green", "red", "white", "orange", "yellow", "blue", "black", "pink",
                                                 "black"])
pitch_length = st.number_input("Pitch Length", value=22, step=1)
if st.button("Assess"):
    if colour is not None:
        if pitch_length <= 0:
            st.warning("Set Pitch Length correctly")
            st.stop()

        else:
            temp_dir = tempfile.gettempdir()
            video_path = os.path.join(temp_dir, video.name)

            with open(video_path, "wb") as f:
                f.write(video.getbuffer())
            assessment = cricket.classify_overall(video_path, colour, pitch_length)
            st.markdown(f'''Bowling: {assessment["ball"]}
Batting: {assessment["bat"]}''')
