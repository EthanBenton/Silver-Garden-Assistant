/*
CREATE TABLE IF NOT EXISTS gardenTable (
    gardenID INTEGER PRIMARY KEY,
    gardenName TEXT NOT NULL,
    gardenLocation TEXT NOT NULL UNIQUE,
    gardenSize TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS weatherTable (
    weatherID INTEGER PRIMARY KEY,
    FOREIGN KEY (gardenID) REFERENCES gardenTable(gardenID),
    timestampNum INTEGER NOT NULL,
    numValues INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS sensorDataTable (
    dataID INTEGER PRIMARY KEY AUTOINCREMENT,
    tStamp INTEGER NOT NULL,
    numValues INTEGER NOT NULL,
    FOREIGN KEY (sensorID) REFERENCES sensorTable(sensorID)
);
*/

CREATE TABLE IF NOT EXISTS sensorTable (
    sensorID INTEGER PRIMARY KEY AUTOINCREMENT,
    sensorType INTEGER NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS sensorValues (
    dataID INTEGER PRIMARY KEY AUTOINCREMENT,
    sensorID INTEGER NOT NULL,
    tStamp INTEGER NOT NULL,
    temperature INTEGER NOT NULL,
    humidity INTEGER NOT NULL,
    FOREIGN KEY (sensorID) REFERENCES sensorTable(sensorID)
);

INSERT OR IGNORE INTO sensorTable (sensorType) VALUES ('TemperatureAndHumidity');

INSERT INTO sensorValues (sensorID, tStamp, temperature, humidity)
SELECT
    (SELECT sensorID FROM sensorTable WHERE sensorType = 'TemperatureAndHumidity'),
    datetime('now'),
    temperature,
    humidity
FROM
    sensorData;
