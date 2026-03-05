# Reddit Gaming Trend Monitor (Local Script)

**Notice to Reddit API Review Team:**
This repository serves as the documentation for my API access request. 

## Project Overview
This is a lightweight, local Python script designed for personal hobbyist data analysis. It fetches public, read-only data from specific gaming subreddits (e.g., r/Genshin_Impact) to analyze patch note discussions and community sentiment.

## Compliance with Responsible Builder Policy
- **NO AI/ML:** Data is temporarily processed in local memory to generate visual charts. It is NEVER used to train, test, or validate any AI/ML models.
- **NO Commercialization:** This is a strictly personal, offline tool. No data is sold or shared.
- **100% Read-Only:** The script only executes `GET` requests. It contains no functions to `POST`, `PUT`, `DELETE`, comment, or upvote.
- **Rate Limiting:** The script utilizes `time.sleep(10)` between requests to strictly ensure no more than 6 requests per minute, staying well below the 100 req/min limit.

## Architecture
- Language: Python 3.x
- Key Libraries: `requests`, `pandas`, `matplotlib`
- Environment: Local desktop offline environment (Incompatible with Devvit).
