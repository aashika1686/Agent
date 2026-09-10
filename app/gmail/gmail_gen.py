import os
import json
import re
import time
import random
import urllib.request
import urllib.error

API_KEY = os.getenv("GEMINI_API_KEY","")
MODEL = os.getenv("GEMINI_MODEL","gemini-3.5-flash")

def generate_email_with_gemini(command):
  if not API_KEY:
    raise RunTimeError("GEMINI_API_KEY is missing.")

  prompt = f"""
You are professional Gmail email writing assistant.

Convert the user's voice command into a professional email.

Rules:
- Do not copy the command literally.
- Do not explain anything.
- Do not invent names, dates, prices, compaines, attachments, or facts.
- Keep the email natural and concise.
- Include an approprriate greeting and closing.

Output exactly :

  SUBJECT: <subject>
  
