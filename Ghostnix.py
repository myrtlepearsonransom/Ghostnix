import time
import datetime
import random
import logging

SUSPICIOUS_NODES = [
    "ghost-relay-01",
    "xmr-mixer-42",
    "zkp-bridge-09",
    "darkpool-17"
]

class GhostnixTracker:
    def __init__(self, interval=300):
        self.interval = interval
        logging.basicConfig(
            level=logging.INFO,
            format='[%(asctime)s] %(levelname)s: %(message)s',
            datefmt='%H:%M:%S'
        )

    def simulate_network_probe(self):
        """Симуляция сетевых метаданных узлов."""
        return [
            {
                "node": node,
                "last_seen": datetime.datetime.utcnow().isoformat(),
                "tx_count": random.randint(0, 4),
                "connections": random.randint(10, 50),
                "latency": round(random.uniform(20, 200), 2)
            }
            for node in SUSPICIOUS_NODES
        ]

    def detect_ghost_activity(self, metadata):
        """Ищет аномалии, характерные для скрытых/маскирующихся узлов."""
        alerts = []
        for node in metadata:
            if node["tx_count"] == 0 and node["connections"] > 30:
                alerts.append((node["node"], "Suspiciously connected but silent"))
            if node["latency"] > 150:
                alerts.append((node["node"], "High latency may indicate proxy obfuscation"))
        return alerts

    def run(self):
        while True:
            logging.info("Scanning network...")
            meta = self.simulate_network_probe()
            alerts = self.detect_ghost_activity(meta)

            if alerts:
                for node, issue in alerts:
                    logging.warning(f"[ALERT] Node: {node} — {issue}")
            else:
                logging.info("No anomalies detected.")
            time.sleep(self.interval)
