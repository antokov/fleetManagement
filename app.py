from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data to simulate database
fleet = [
    {"id": 1, "name": "Tesla Model S", "kilometers": 45000, "next_service": "2024-11-15", "battery": 85, "last_service": "2024-05-10", "insurance": "2024-12-31"},
    {"id": 2, "name": "BMW X5", "kilometers": 60000, "next_service": "2025-01-05", "battery": 50, "last_service": "2024-03-01", "insurance": "2025-02-20"},
    {"id": 3, "name": "Audi Q7", "kilometers": 30000, "next_service": "2024-12-10", "battery": 70, "last_service": "2024-04-20", "insurance": "2025-08-15"}
]

vehicles_for_rent = [
    {"id": 1, "name": "Nissan Leaf", "availability": "available", "duration": [1, 3, 5]},
    {"id": 2, "name": "Chevrolet Bolt", "availability": "available", "duration": [1, 3, 5]},
    {"id": 3, "name": "Volkswagen ID.4", "availability": "available", "duration": [1, 3, 5]}
]

# Routes
@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/fleet')
def fleet_overview():
    return render_template('fleet_overview.html', fleet=fleet)

@app.route('/vehicle/<int:id>')
def vehicle_details(id):
    vehicle = next((v for v in fleet if v["id"] == id), None)
    if vehicle:
        return render_template('vehicle_details.html', vehicle=vehicle)
    else:
        return "Vehicle not found", 404

@app.route('/order')
def order_new_vehicle():
    return render_template('order_new_vehicle.html', vehicles=vehicles_for_rent)

@app.route('/services')
def services():
    return render_template('services.html')

if __name__ == "__main__":
    app.run(debug=True)
