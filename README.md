# VRMS API
 
---
 
# Development
 
## Requirements
 
- Docker
- Python 3.13+ (only for local LSP support, not required to run the app)
 
---
 
## Running the App (Docker)
 
Build the image:
 
```bash
docker build -t vrms .
```
 
Run the container:
 
```bash
docker run --rm -p 3004:8000 -v $(pwd):/app vrms
```
 
The API will be available at `http://localhost:3004`.
 
---
 
## LSP Setup (Neovim / Pyright)
 
This is only needed for editor support (autocomplete, type checking). The app itself runs entirely in Docker.
 
Create and activate a virtual environment:
 
```bash
python3 -m venv venv
source venv/bin/activate
```
 
Install dev dependencies:
 
```bash
pip install -r requirements-dev.txt
```
 
Deactivate when done:
 
```bash
deactivate
```
 
Make sure your `pyrightconfig.json` has:
 
```json
{
  "venvPath": ".",
  "venv": "venv"
}
```
 
---
 
# Production
 
> To be documented.

