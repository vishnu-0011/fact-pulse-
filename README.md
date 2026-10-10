• Quick start: cp .env.example .env && make demo 
• Services table (8 services with ports and descriptions) 
• Datasets table (C-MAPSS, IMS Bearings, AI4I 2020) 
• Milestone roadmap (M1 through M6) 

Architecture Decision Records 

    ADR-001: Anomaly Detection Ensemble 

        Decision: LSTM Autoencoder + Isolation Forest ensemble 
        Why LSTM-AE: Catches gradual degradation via temporal reconstruction error 
        Why Isolation Forest: Catches sudden point anomalies the LSTM may smooth over 
        Why adaptive thresholds: Per-machine calibration prevents alarm fatigue 

    ADR-002: Shadow Deployment 
    
        Decision: Staging models score alongside Production — logged, never acted upon 
        Why: Offline metrics don't guarantee real-world performance 
        Promotion: Only after shadow period proves equivalent or better results 
        Trade-off: 2x compute during shadow (acceptable for safety-critical domain)