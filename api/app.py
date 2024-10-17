from flask import Flask, jsonify
import random
from prometheus_client import Counter, Gauge, generate_latest

app = Flask(__name__)

# Prometheus metrics
FEED_COUNTER = Counter('pet_feeds_total', 'Total number of times the pet has been fed')
PLAY_COUNTER = Counter('pet_plays_total', 'Total number of times the pet has been played with')
HAPPINESS_GAUGE = Gauge('pet_happiness', 'Current happiness level of the pet')
HUNGER_GAUGE = Gauge('pet_hunger', 'Current hunger level of the pet')

# Initialize pet state
happiness = 50
hunger = 50

@app.route('/feed')
def feed_pet():
    global hunger
    hunger = max(0, hunger - random.randint(5, 15))
    FEED_COUNTER.inc()
    HUNGER_GAUGE.set(hunger)
    return jsonify({"message": "Pet fed!", "hunger": hunger})

@app.route('/play')
def play_with_pet():
    global happiness
    happiness = min(100, happiness + random.randint(5, 15))
    PLAY_COUNTER.inc()
    HAPPINESS_GAUGE.set(happiness)
    return jsonify({"message": "Played with pet!", "happiness": happiness})

@app.route('/status')
def get_status():
    return jsonify({
        "happiness": happiness,
        "hunger": hunger
    })

@app.route('/metrics')
def metrics():
    return generate_latest()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
