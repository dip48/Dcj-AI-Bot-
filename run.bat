@cls


if exist data\ChatLot.json (
    del data\ChatLot.json
    echo data\ChatLot.json deleted.
) else (
    echo ChatLot.json not found in data folder.
)

py run.py

