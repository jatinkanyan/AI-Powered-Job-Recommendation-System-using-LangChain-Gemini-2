import json

def load_jobs_from_file(filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        jobs_data = json.load(f)

    # If the JSON has a "results" key (API-style), use that list; else assume it's already a list
    if isinstance(jobs_data, dict) and "results" in jobs_data:
        jobs_data = jobs_data["results"]

    jobs = []
    for job in jobs_data:
        title = job.get("title", "No Title")

        # Handle both flat and nested company formats
        company = (
            job.get("companyName") or
            (job.get("company", {}).get("display_name") if isinstance(job.get("company"), dict) else job.get("company"))
            or "Unknown"
        )

        # Handle both flat and nested location formats
        location = (
            job.get("location") if isinstance(job.get("location"), str)
            else (job.get("location", {}).get("display_name") if isinstance(job.get("location"), dict) else "Not Specified")
        )

        desc = job.get("description", "")

        combined_text = f"{title} at {company} ({location})\n{desc}"

        jobs.append({
            "id": job.get("id", ""),
            "title": title,
            "company": company,
            "location": location,
            "description": desc,
            "text": combined_text
        })

    return jobs