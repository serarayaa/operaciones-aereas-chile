import ast
import csv
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "data" / "operaciones-aeropuertos.csv"
NOTEBOOK_PATH = ROOT / "notebooks" / "Proyecto_Operaciones_Aereas_Chile_COLAB.ipynb"
EXPECTED_COLUMNS = {
    "mes_id",
    "aeropuerto_oaci",
    "internacional_domestico",
    "cnt_operaciones",
}


def load_rows():
    with CSV_PATH.open(encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def test_required_files_exist():
    assert CSV_PATH.is_file()
    assert NOTEBOOK_PATH.is_file()


def test_csv_schema_and_size():
    rows = load_rows()
    assert len(rows) >= 10_000
    assert set(rows[0]) == EXPECTED_COLUMNS


def test_csv_quality_rules():
    rows = load_rows()
    assert all(all(value != "" for value in row.values()) for row in rows)
    assert len(rows) == len({tuple(row[column] for column in sorted(row)) for row in rows})
    assert all(int(row["cnt_operaciones"]) >= 0 for row in rows)
    assert {row["internacional_domestico"] for row in rows} <= {"D", "I"}


def test_csv_month_format_and_range():
    rows = load_rows()
    months = [int(row["mes_id"]) for row in rows]
    assert min(months) == 200001
    assert max(months) >= 202606
    assert all(1 <= month % 100 <= 12 for month in months)


def test_notebook_is_executed_without_errors():
    notebook = json.loads(NOTEBOOK_PATH.read_text(encoding="utf-8"))
    code_cells = [cell for cell in notebook["cells"] if cell["cell_type"] == "code"]
    assert code_cells
    assert all(cell.get("execution_count") is not None for cell in code_cells)
    output_types = Counter(
        output.get("output_type")
        for cell in code_cells
        for output in cell.get("outputs", [])
    )
    assert output_types["error"] == 0
    assert output_types["display_data"] >= 1


def test_notebook_python_syntax():
    notebook = json.loads(NOTEBOOK_PATH.read_text(encoding="utf-8"))
    for index, cell in enumerate(notebook["cells"]):
        if cell["cell_type"] == "code":
            ast.parse("".join(cell.get("source", [])), filename=f"cell_{index}")

