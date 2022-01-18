import setuptools

with open("README.md", "r+") as f:
    print("opened")
    long_de = f.read()


setuptools.setup(
    name="spotidnldr",  # Replace with your own username
    version="v1.3.0",
    author="Rohit Patil",
    author_email="rahulhimesh09@gmail.com",
    description="the spotify song downloader",
    download_url="https://github.com/raprocks/spotidnldr/archive/v1.0.1.tar.gz",
    long_description=long_de,
    long_description_content_type="text/markdown",
    url="https://github.com/raprocks/spotindnldr",
    license="GPLv3+",
    packages=[
        "spotidnldr",
    ],
    package_data={"spotidnldr": ["static/*", "templates/*"]},
    install_requires=[
        "spotipy",
        "youtube-dl",
        "eyeD3",
        "requests",
        "pytube",
        "click",
        "ffmpeg-python",
        "ytmusicapi",
    ],
    classifiers=[
        "Natural Language :: English",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    entry_points="""
        [console_scripts]
        spoti=spotidnldr.clifi:cli
    """,
    python_requires=">=3.6",
    include_package_data=True,
)
