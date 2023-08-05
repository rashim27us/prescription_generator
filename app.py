<!DOCTYPE html>
<html>
<head>
    <title>Prescription Generator</title>
</head>
<body>
    <h1>Prescription Generator</h1>
    <form action="/submit" method="post" enctype="multipart/form-data">
        <label for="patient_name">Patient Name:</label>
        <input type="text" id="patient_name" name="patient_name" required><br>

        <label for="age">Age:</label>
        <input type="number" id="age" name="age" required><br>

        <label for="gender">Gender:</label>
        <input type="radio" id="male" name="gender" value="Male" required>
        <label for="male">Male</label>
        <input type="radio" id="female" name="gender" value="Female" required>
        <label for="female">Female</label><br>

        <!-- Add other fields here for patient ID, prescription ID, symptoms, disease, lab report, etc. -->

        <label for="lab_report">Lab Report:</label>
        <input type="file" id="lab_report" name="lab_report"><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
