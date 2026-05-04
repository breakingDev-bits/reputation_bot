from datetime import datetime
from pathlib import Path
# cfg
from cfg import LOGS_PATH


logsFile = Path(LOGS_PATH)

async def printAndLog(*args) -> None:
    text = " ".join(map(str, args))
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_message = f"[{timestamp}] {text}"

    print(full_message)

    with logsFile.open(mode="a", encoding="utf-8") as f:
        f.write(full_message + "\n")
