import argparse
import json
from datetime import date
from pathlib import Path

DATA_FILE = Path("cuniculture_data.json")

class CunicultureManager:
    def __init__(self, data_file=DATA_FILE):
        self.data_file = Path(data_file)
        self.data = {"rabbits": [], "resources": [], "waste": []}
        self._load()

    def _load(self):
        if self.data_file.exists():
            try:
                with self.data_file.open("r", encoding="utf-8") as f:
                    self.data = json.load(f)
            except json.JSONDecodeError:
                self.data = {"rabbits": [], "resources": [], "waste": []}

    def _save(self):
        with self.data_file.open("w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)

    # Rabbit management
    def add_rabbit(self, breed, cage, age):
        self.data["rabbits"].append({"breed": breed, "cage": cage, "age": age})
        self._save()

    def list_rabbits(self):
        return list(self.data.get("rabbits", []))

    # Resource management
    def add_resource(self, rtype, quantity, unit, rdate):
        self.data["resources"].append({
            "type": rtype,
            "quantity": quantity,
            "unit": unit,
            "date": rdate,
        })
        self._save()

    def list_resources(self):
        return list(self.data.get("resources", []))

    # Waste management
    def add_waste(self, wtype, quantity, unit, wdate):
        self.data["waste"].append({
            "type": wtype,
            "quantity": quantity,
            "unit": unit,
            "date": wdate,
        })
        self._save()

    def list_waste(self):
        return list(self.data.get("waste", []))


def main(argv=None):
    parser = argparse.ArgumentParser(description="Cuniculture Management CLI")
    sub = parser.add_subparsers(dest="command")

    # Rabbit commands
    p_add_rabbit = sub.add_parser("add-rabbit", help="Add a new rabbit")
    p_add_rabbit.add_argument("breed", help="Breed of the rabbit")
    p_add_rabbit.add_argument("cage", help="Cage or pen identifier")
    p_add_rabbit.add_argument("age", type=int, help="Age in months")

    sub.add_parser("list-rabbits", help="List all rabbits")

    # Resource commands
    p_add_res = sub.add_parser("add-resource", help="Record resource usage")
    p_add_res.add_argument("type", help="Type of resource")
    p_add_res.add_argument("quantity", type=float, help="Quantity")
    p_add_res.add_argument("unit", help="Unit of measure")
    p_add_res.add_argument("--date", default=str(date.today()), help="Date, default today")

    sub.add_parser("list-resources", help="List recorded resources")

    # Waste commands
    p_add_waste = sub.add_parser("add-waste", help="Record waste")
    p_add_waste.add_argument("type", help="Type of waste")
    p_add_waste.add_argument("quantity", type=float, help="Quantity")
    p_add_waste.add_argument("unit", help="Unit of measure")
    p_add_waste.add_argument("--date", default=str(date.today()), help="Date, default today")

    sub.add_parser("list-waste", help="List recorded waste")

    args = parser.parse_args(argv)
    manager = CunicultureManager()

    if args.command == "add-rabbit":
        manager.add_rabbit(args.breed, args.cage, args.age)
        print("Rabbit added.")
    elif args.command == "list-rabbits":
        rabbits = manager.list_rabbits()
        if not rabbits:
            print("No rabbits recorded.")
        for i, r in enumerate(rabbits, 1):
            print(f"{i}. {r['breed']} - {r['cage']} ({r['age']} months)")

    elif args.command == "add-resource":
        manager.add_resource(args.type, args.quantity, args.unit, args.date)
        print("Resource recorded.")
    elif args.command == "list-resources":
        resources = manager.list_resources()
        if not resources:
            print("No resources recorded.")
        for r in resources:
            print(f"{r['date']}: {r['type']} - {r['quantity']} {r['unit']}")

    elif args.command == "add-waste":
        manager.add_waste(args.type, args.quantity, args.unit, args.date)
        print("Waste recorded.")
    elif args.command == "list-waste":
        waste = manager.list_waste()
        if not waste:
            print("No waste recorded.")
        for w in waste:
            print(f"{w['date']}: {w['type']} - {w['quantity']} {w['unit']}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
