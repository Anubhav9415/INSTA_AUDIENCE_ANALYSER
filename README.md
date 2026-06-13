# Instagram Audience Persona Analyzer (Compliant)

Classify bios/comments into personas (Student, Tech, Religious, Fitness, Job-seeker, Creator, Business, Other) and generate an aggregate report.  
**No scraping**. Works with official Instagram Graph API data you’re allowed to fetch (audience insights, commenters/likers on your media) or CSV uploads collected **with consent**.

Analyze your Instagram audience personas 
Built with Python · FastAPI · Chart.js · CSV Upload · Docker-ready.
Just clone → install → run → see charts in your browser 🚀


After following the web api will be running on 
http://127.0.0.1:8000/ui


git clone https://github.com/Anubhav9415/INSTA_AUDIENCE_ANALYSER.git
cd INSTA_AUDIENCE_ANALYSER

macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

Windows (PowerShell)
python -m venv .venv
.venv\Scripts\Activate
pip install -r requirements.txt


Run the Demo (no Instagram needed)
python -m scripts.demo_classify     # Creates data/report.json with audience categories (students, tech, fitness, etc.).

uvicorn app.main:app --reload --port 8000

Open in your browser:

API docs: http://127.0.0.1:8000/docs

Web UI: http://127.0.0.1:8000/ui

👉 In the Web UI:

Click “Load Demo Data” to see sample charts.

Or Upload a CSV with columns id,bio.
example csv
id,bio
user1,B.Tech CSE | Learning DSA and ML
user2,Gym Trainer | Calisthenics
user3,Entrepreneur | Startup founder | Ecommerce


Customize Personas
Edit app/classifier.py → update keywords inside BUCKETS.
Restart the server to apply changes.

Run with Docker (optional)
docker build -t insta-audience .
docker run --rm -p 8000:8000 insta-audience

Then open http://127.0.0.1:8000/ui



Once you are here and understand the code and the working, proceed to add instagram apis and advance the project.


---

## TL;DR – Clone & Run

```bash
git clone https://github.com/<you>/insta_audience_tool.git
cd insta_audience_tool

make bootstrap     # creates venv + installs deps
make demo          # runs demo on data/sample_bios.csv -> data/report.json
make api           # starts API at http://127.0.0.1:8000/docs
```

If you don’t have `make`:
```bash
python -m venv .venv
source .venv/bin/activate               # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m scripts.demo_classify
uvicorn app.main:app --reload --port 8000
```

---

## Endpoints

- `GET /health` – liveness probe
- `GET /docs/ig` – notes on Graph API wiring (no scraping)
- `POST /classify` – classify items `{id,text}`
- `POST /report` – classify + aggregate in one shot

Open Swagger: `http://127.0.0.1:8000/docs`

### Example payload
```json
{
  "items": [
    {"id":"u1","text":"B.Tech CSE @ IIT. Learning DSA and ML. Open to work"},
    {"id":"u2","text":"Gym • Personal Trainer • Calisthenics"},
    {"id":"u3","text":"Entrepreneur | Startup founder | Ecommerce"}
  ]
}
```

---

## Configure Personas

Edit keywords in `app/classifier.py` under `BUCKETS`. Tailor for IIT/GATE/tech jobs/creators, etc. Changes take effect on restart.

Optional zero-shot (slower, smarter):
```bash
pip install "transformers==4.44.2" torch
export USE_ZEROSHOT=true
export ZS_MODEL=facebook/bart-large-mnli
uvicorn app.main:app --reload
```

---

## Instagram (Compliant Flow)

1. Switch your IG to **Business/Creator**.
2. Create a Facebook App → get `FB_APP_ID` / `FB_APP_SECRET`.
3. OAuth → Page token → exchange for **long‑lived** Page token.
4. Get **IG Business Account ID**.
5. Pull **audience insights** and **comments/likers** (where permitted).
6. Feed comment/bio text (where consented) into `POST /classify`; aggregate via `POST /report`.

Followers’ bios are **not** exposed via Graph API. Don’t scrape. See `app/ig_api.py` and `GET /docs/ig` for endpoint notes.

---

## Docker

```bash
docker build -t insta-audience .
docker run --rm -p 8000:8000 --env-file .env.example insta-audience
# http://127.0.0.1:8000/docs
```

**Compose:**
```bash
docker-compose up --build
```

---

## Devcontainer (VS Code)

Open folder → “Reopen in Container”. You’ll get Python with dependencies preinstalled.

---

## Contributing & Troubleshooting

- See **CONTRIBUTING.md** for PR guidelines.
- See **TROUBLESHOOTING.md** for fixes like `ModuleNotFoundError: app`, `uvicorn` not found, and Graph API 403s.

---

## License

MIT. See `LICENSE`.
