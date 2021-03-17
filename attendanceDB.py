def markAttendance(rollNumber, timestamp, mydb):

    query = {'rollNumber': rollNumber, 'timeStamp': timestamp}
    resultQuery = mydb.attendanceTrack.insert_one(query)
    if resultQuery.inserted_id:
        return True
    else:
        return False
