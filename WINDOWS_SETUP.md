# 🪟 Windows Setup Guide

## ❌ Error: 'streamlit' is not recognized

This happens when Streamlit isn't installed or not in your PATH. Here are **3 solutions**:

---

## ✅ Solution 1: Use Python Module Method (RECOMMENDED)

Instead of `streamlit run app.py`, use:

```bash
python -m streamlit run app.py
```

This works even if `streamlit` command isn't in your PATH.

---

## ✅ Solution 2: Install Streamlit First

If Streamlit isn't installed, run:

```bash
python -m pip install streamlit
```

Or:

```bash
pip install streamlit
```

Then verify installation:

```bash
python -m streamlit --version
```

---

## ✅ Solution 3: Install All Dependencies

Install everything at once:

```bash
python -m pip install -r requirements.txt
```

Or individually:

```bash
python -m pip install streamlit
python -m pip install openai
python -m pip install python-dotenv
```

---

## 🚀 Running the App (Choose One Method)

### Method 1: Python Module (Most Reliable)
```bash
python -m streamlit run app.py
```

### Method 2: Direct Command (If PATH is set)
```bash
streamlit run app.py
```

### Method 3: With Specific Port
```bash
python -m streamlit run app.py --server.port 8501
```

---

## 🔍 Troubleshooting

### Check if Python is installed:
```bash
python --version
```

### Check if pip is working:
```bash
python -m pip --version
```

### If you get "python is not recognized":
- Make sure Python is installed
- Add Python to your PATH
- Or use `py` instead of `python`:
  ```bash
  py -m streamlit run app.py
  ```

### If you get permission errors:
```bash
python -m pip install --user streamlit
```

---

## ✅ Success Indicators

When it works, you'll see:
```
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
Network URL: http://192.168.x.x:8501
```

The browser should open automatically!

---

## 📝 Quick Commands Reference

```bash
# Install dependencies
python -m pip install -r requirements.txt

# Run the app
python -m streamlit run app.py

# Stop the app
Press Ctrl+C in the terminal
```

---

**Most Common Solution:** Use `python -m streamlit run app.py` instead of `streamlit run app.py`






