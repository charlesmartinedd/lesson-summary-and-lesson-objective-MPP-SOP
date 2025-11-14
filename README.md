# MPP Lesson Objectives and Summaries

Interactive HTML learning materials for the Mentor-Protégé Program (MPP), designed for Articulate Rise integration.

## Overview

This repository contains learning objectives and lesson summaries for the DoD Mentor-Protégé Program training modules. Content is generated using Google Gemini File Search API based on MPP SOP and DFARS Appendix I documentation.

## Contents

- **Module 1/Lesson 1/lesson_objectives.html** - Interactive display of 5 MPP learning objectives with reference buttons to MPP SOP and Appendix I sections
- **Module 1/Lesson 1/lesson_summary.html** - Interactive topic cards with learning objectives and 2-3 sentence summaries
- **Module_1_Lesson_1.py** - Python script with lesson data and File Search integration for interactive Q&A

## Features

- Clean, professional UI with modal dialogs
- Responsive design for all devices
- All "Mentor" and "Protégé" properly capitalized throughout
- Keyboard navigation support (Escape to close modals)
- Smooth animations and transitions
- Ready for Articulate Rise integration

## Setup (for Python script)

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Add your Google API key to `.env`:
   ```
   GOOGLE_API_KEY=your_actual_api_key_here
   ```

3. Install dependencies:
   ```bash
   pip install google-genai
   ```

4. Run the interactive lesson:
   ```bash
   python Module_1_Lesson_1.py
   ```

## File Search Store

The content is generated from the following File Search Store:
- **Store ID**: `fileSearchStores/mppsopdocumentation-j83n2w5zjn96`
- **Model**: `gemini-2.5-flash`

## Usage in Articulate Rise

1. Open Articulate Rise
2. Create a new block
3. Select "Embed" or "HTML" block type
4. Copy the contents of `lesson_objectives.html` or `lesson_summary.html`
5. Paste into the embed block
6. Preview and publish

## Structure

### Lesson Objectives HTML
- List of 5 learning objectives
- "Find in SOP/Appendix I" buttons
- Modal displays document references (source + section numbers)

### Lesson Summary HTML
- Topic cards with emojis and learning objectives
- Click to open modal with 2-3 sentence summary
- Clean, scannable format

## Technologies

- HTML5 semantic markup
- CSS3 with flexbox and grid layouts
- Vanilla JavaScript (no dependencies)
- Google Gemini File Search API (Python script only)

## License

Generated with [Claude Code](https://claude.com/claude-code)

## Contact

Alexandria's Design - charlesmartinedd@gmail.com
