CREATE TABLE IF NOT EXISTS gardenTable (
    gardenID INTEGER PRIMARY KEY,
    gardenName TEXT NOT NULL,
    gardenLocation TEXT NOT NULL UNIQUE,
    gardenSize TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS sensorTable (
    sensorID INTEGER PRIMARY KEY,
    sensorType INTEGER NOT NULL,
    FOREIGN KEY (gardenID) REFERENCES gardenTable(gardenID)
);

CREATE TABLE IF NOT EXISTS weatherTable (
    weatherID INTEGER PRIMARY KEY,
    FOREIGN KEY (gardenID) REFERENCES gardenTable(gardenID),
    timestampNum INTEGER NOT NULL,
    numValues INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS sensorDataTable (
    dataID INTEGER PRIMARY KEY,
    FOREIGN KEY (sensorID) REFERENCES sensorTable(sensorID),
    timestampNum INTEGER NOT NULL,
    numValues INTEGER NOT NULL
);