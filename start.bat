if exist venv\ (
    echo "Setup is already done."
    cmd /k "venv\Scripts\activate && py main.py"
) else (
    echo "Setting up environment."
    cmd /k "py -m venv venv && venv\Scripts\activate && pip install -r requirements.txt && py main.py"
)