import {
  enablePromise,
  openDatabase,
  SQLiteDatabase,
} from 'react-native-sqlite-storage';

// Enable promise for SQLite
enablePromise(true)

export const connectToDatabase = async () => {
  return openDatabase(
    { name: "routine.db", location: "default" },
    () => {},
    (error) => {
      console.error(error)
      throw Error("Could not connect to database")
    }
  ) 
}

export const createTables = async (db: SQLiteDatabase) => {
  const profileQuery = `
   CREATE TABLE IF NOT EXISTS Profile (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      firstName TEXT,
      lastName TEXT,
      email TEXT
   )
  `
  //days of Week is a bitmask representing the days the routine occurs on
  // Mon = 1, Tue = 2, Wed = 4, Thu = 8, Fri = 16, Sat = 32, Sun = 64
  // visibility: 0 = private, 1 = friends, 2 = public
  const routinesQuery = `
    CREATE TABLE IF NOT EXISTS Routines (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        daysOfWeek INTEGER,
        startTime TEXT,
        endTime TEXT,
        reminderTime TEXT,
        isActive INTEGER DEFAULT 1,
        visibility INTEGER DEFAULT 1,
        FOREIGN KEY (firstRoutineAction) REFERENCES RoutineActions(id)
    )
  `

  const routineActionQuery = `
    CREATE TABLE IF NOT EXISTS RoutineActions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        routineId INTEGER,
        actionOrder INTEGER,
        actionIcon TEXT ,
        actionName TEXT,
        actionDescription TEXT,
        actionDuration TEXT,
        autoComplete INTEGER NOT NULL DEFAULT 1,
        FOREIGN KEY (routineId) REFERENCES Routines(id) ON DELETE CASCADE
    )
  `

  const friendsQuery = `
   CREATE TABLE IF NOT EXISTS Friends (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      firstName TEXT,
      lastName TEXT,
      email TEXT UNIQUE
   )
  `

  const routineCompletions = `
   CREATE TABLE IF NOT EXISTS RoutineCompletions (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      routineID INTEGER,
      date DATE NOT NULL,
      completedAt DATETIME DEFAULT CURRENT_TIMESTAMP,
      UNIQUE (routineID, date),
      FOREIGN KEY (routineID) REFERENCES Routines(id)
   )
  `
  const routineActionCompletions = `
    CREATE TABLE IF NOT EXISTS RoutineActionCompletions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        routineActionId INTEGER NOT NULL,
        date DATE NOT NULL,
        startedAt DATETIME,
        completedAt DATETIME,
        UNIQUE (routineActionId, date),
        FOREIGN KEY (routineActionId) REFERENCES RoutineActions(id) ON DELETE CASCADE
    );
  `

  try {
    await db.executeSql(routinesQuery)
    await db.executeSql(friendsQuery)
    await db.executeSql(routineActionCompletions)
    await db.executeSql(routineCompletions)
    await db.executeSql(routineActionQuery)
    await db.executeSql(profileQuery)
  } catch (error) {
    console.error(error)
    throw Error(`Failed to create tables`)
  }
}