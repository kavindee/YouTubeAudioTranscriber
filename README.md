# YouTube Whisper Transcriber

[![YouTube](https://img.shields.io/badge/YouTube-red?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/)
![GitHub](https://img.shields.io/github/license/your-username/YouTubeWhisperTranscriber)
![GitHub stars](https://img.shields.io/github/stars/your-username/YouTubeWhisperTranscriber?style=social)

## Overview

YouTube Whisper Transcriber is a Python script that allows users to download audio from a YouTube video and transcribe it using the Whisper ASR (Automatic Speech Recognition) model. The script utilizes the `pytube` library for YouTube audio download and the `whisper` library for ASR transcription. The transcribed text is then saved in a text file for easy reference.

## Features

- **YouTube Audio Download:** Utilizes `pytube` to download audio from a specified YouTube video.
- **Whisper ASR Transcription:** Transcribes the downloaded audio using the Whisper ASR model.
- **Text File Creation:** Saves the transcribed text in a text file for easy access.

## How to Use

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/YouTubeWhisperTranscriber.git

2. create environment
    ```bash
   python -m venv venv

   ```bash
   .\venv\Scripts\activate
    
3. Install the required dependencies:

   ```bash
   pip install openai-whisper pytube
