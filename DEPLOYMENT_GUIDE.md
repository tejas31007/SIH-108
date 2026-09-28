# How to Go Live with BharatStandards AI (SIH-108)

This guide explains how to take this project live to the internet with a public HTTPS link.

---

## 💡 Important Context About This Project
Unlike a simple static HTML website, this project is a **Full-Stack AI Application**:
- **Backend:** Python FastAPI (`rank-bm25`, `scikit-learn`, `pymupdf` for parsing PDF tenders, `python-docx`).
- **Frontend:** Responsive dashboard served directly by the backend at `/`.

Because of this, the best hosting platforms are those that natively support **Python Web Services**.

---

## 🚀 Option 1: Render.com (Recommended — 100% Free, Permanent Cloud URL)

Render is the standard, best free platform for Python FastAPI applications. It has no serverless timeout limits and supports all Python libraries.

### Step 1: Push your code to GitHub
1. Open your terminal in this project folder (`C:\Users\tejal\OneDrive\Desktop\SIH-108`).
2. Go to [github.com](https://github.com) and create a new **public or private repository** named `SIH-108`.
3. In your terminal, run:
   ```bash
   git remote add origin https://github.com/YOUR_GITHUB_USERNAME/SIH-108.git
   git branch -M main
   git push -u origin main
   ```

### Step 2: Deploy on Render
1. Go to **[render.com](https://render.com)** and sign in with your GitHub account (free).
2. Click the blue **"New +"** button at the top right and select **"Web Service"**.
3. Select your `SIH-108` repository.
4. Render will auto-detect everything, but verify these settings:
   - **Name:** `bharatstandards-ai` (or any name you choose)
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
   - **Plan:** Free
5. Click **"Deploy Web Service"**.
6. Within 2 to 3 minutes, Render will build and deploy it, giving you a live URL like:
   `https://bharatstandards-ai.onrender.com`

---

## ⚡ Option 2: Instant Live URL in 10 Seconds (Localtunnel / Ngrok — No Sign-up, No GitHub)

If you need a live public URL **right now** to test on your phone, show a mentor, or demo in a meeting directly from your computer without uploading code anywhere:

1. Make sure your server is running in terminal:
   ```bash
   python run_server.py
   ```
2. Open a **second terminal** and run:
   ```bash
   npx localtunnel --port 8000
   ```
   *(or if you have ngrok installed: `ngrok http 8000`)*
3. It will immediately print a public HTTPS URL like:
   `https://bright-stars-glow.loca.lt`
4. Anyone on any device in the world can open that URL and interact with your live application!

---

## ▲ Option 3: Vercel (Serverless Python)

We have already created the required configuration files for Vercel:
- [`vercel.json`](file:///C:/Users/tejal/OneDrive/Desktop/SIH-108/vercel.json)
- [`api/index.py`](file:///C:/Users/tejal/OneDrive/Desktop/SIH-108/api/index.py)

### Steps to Deploy on Vercel:
1. Push your code to GitHub (as described in Option 1).
2. Go to **[vercel.com](https://vercel.com)** and log in.
3. Click **"Add New..."** $\to$ **"Project"**.
4. Import your `SIH-108` repository.
5. In **Framework Preset**, select **"Other"**.
6. Click **"Deploy"**.

> [!NOTE]
> Vercel uses AWS Lambda under the hood with a 250MB uncompressed bundle limit for serverless functions. If Vercel gives a package size warning due to heavy ML libraries (`scikit-learn` / `pymupdf`), **Render.com (Option 1)** is the guaranteed, recommended alternative because it runs as a dedicated Python web service without serverless constraints.

---

## 🚂 Option 4: Railway.app

1. Go to **[railway.app](https://railway.app)**.
2. Click **"New Project"** $\to$ **"Deploy from GitHub repo"**.
3. Select `SIH-108`.
4. Railway will automatically detect the [`Procfile`](file:///C:/Users/tejal/OneDrive/Desktop/SIH-108/Procfile) and deploy it immediately with free monthly credits.
