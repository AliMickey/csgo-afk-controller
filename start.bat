if exist venv\ (
    echo "Setup is already done"
) else (
    echo "Setting up environment"
    cmd /k "py -m venv venv && venv\Scripts\activate && pip install -r requirements.txt"
)
cls
cmd /k "venv\Scripts\activate && py main.py"