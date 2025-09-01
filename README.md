# Resi-builder

Create a resume and cover letter

## Installation

```
pip install resi-builder
```

## Build User History

The following can be a JSON file or a python dictionary

```
{
  "contact_info": {
    "name": "",
    "phone": "",
    "email": "",
    "linkedIn": ""
  },
  "education": [
    {
      "school": "",
      "degree": "",
      "field_of_study": "",
      "location": ""
    }
  ],
  "history": [
    {
      "role": "",
      "company": "",
      "dates": "",
      "experience": [],
      "industry": []
    }
  ],
  "activities_and_interests": "",
  "profile": "",
  "skills": []
}
```

## Build Resume

In order to make a preview resume use the following


```python
import resi

# Job metadata
metadata = {
    'hiring_manager': '',
    'job_desc': 'Job Description'
}

# Build the preview data
resume_data =  resi.resume.build_resume_preview(metadata, user_history)

# Be sure to preview the data before building the final file

# Build the final PDF file
resi.resume.build_resume_pdf(resume_data, user_history)

```

## Build Cover Letter

```python
import resi

# Job metadata
metadata = {
    'hiring_manager': '',
    'job_desc': 'Job Description'
}

# Build the preview data
cover_letter_data = resi.cover_letter.build_cover_letter_preview(metadata, user_history)

# Be sure to preview the data before building the final file

# Build the final PDF file
resi.cover_letter.build_cover_letter_pdf(cover_letter_data, user_history)
```


