CREATE EXTENSION IF NOT EXISTS timescaledb;

-- Hypertable: auto-partitioned by day 
CREATE TABLE telemetry ( 
    ts TIMESTAMPTZ NOT NULL, 
    machine_id VARCHAR(50) NOT NULL, 
    sensor_id VARCHAR(100) NOT NULL, 
    value DOUBLE PRECISION NOT NULL, 
    quality SMALLINT DEFAULT 0 ); 

SELECT create_hypertable('telemetry', 'ts', chunk_time_interval => INTERVAL '1 day');

-- Continuous aggregate for dashboards 
CREATE MATERIALIZED VIEW telemetry_hourly 
WITH (timescaledb.continuous) AS 
SELECT time_bucket('1 hour', ts) AS bucket, 
machine_id, sensor_id, AVG(value), MIN(value), MAX(value), 
STDDEV(value), COUNT(*) 
FROM telemetry GROUP BY bucket, machine_id, sensor_id;

-- Retention: raw kept 90 days only 
SELECT add_retention_policy('telemetry', INTERVAL '90 days');
