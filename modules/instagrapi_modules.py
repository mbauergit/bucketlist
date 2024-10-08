from instagrapi import Client
from instagrapi.exceptions import LoginRequired
import logging

logger = logging.getLogger()

def login_user(USERNAME, PASSWORD):
    """
    Attempts to login to Instagram using either the provided session information
    or the provided username and password.
    """

    cl = Client()
    login_via_session = False
    login_via_pw = False

    try:
        session = cl.load_settings("session.json")

        try:
            cl.set_settings(session)
            cl.login(USERNAME, PASSWORD)

            # check if session is valid
            try:
                cl.get_timeline_feed()
                print("Logged in with session")
            except LoginRequired:
                print("Session is invalid, need to login via username and password")

                old_session = cl.get_settings()

                # use the same device uuids across logins
                cl.set_settings({})
                cl.set_uuids(old_session["uuids"])

                cl.login(USERNAME, PASSWORD)
            login_via_session = True
        except Exception as e:
            print("Couldn't login user using session information: %s" % e)

    except:
        if not login_via_session:
            try:
                print("Attempting to login via username and password. username: %s" % USERNAME)
                if cl.login(USERNAME, PASSWORD):
                    login_via_pw = True
                    cl.dump_settings("session.json")
            except Exception as e:
                print("Couldn't login user using username and password: %s" % e)

        if not login_via_pw and not login_via_session:
            raise Exception("Couldn't login user with either password or session")
        
    return cl

# Download video from Instagram post
def download_instagram_video(url, cl):
    url=cl.media_info(cl.media_pk_from_url(url)).video_url
    print("URL:", url)
    # Download the video using the media ID
    video_path = cl.clip_download_by_url(url, folder="downloads")
    print(f"Video downloaded to: {video_path}")
    return