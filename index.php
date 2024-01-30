<?php
  $conn = mysqli_connect(
    'localhost',
    'exampleuser',
    'kick',
    'example'
  );

  if(!$conn){
    echo 'Connection error: ' . mysqli_connect_error();
  }



$sql = 'SELECT * FROM users';
$result = mysqli_query($conn, $sql);

if ($result) {
    echo '<table border="1">';
    echo '<tr><th>ID</th><th>Username</th><th>Password</th></tr>';

    while ($row = mysqli_fetch_assoc($result)) {
        echo '<tr>';
        echo '<td>' . $row['id'] . '</td>';
        echo '<td>' . $row['username'] . '</td>';
        echo '<td>' . $row['password'] . '</td>';
        echo '</tr>';
    }

    echo '</table>';
} else {
    echo 'Error: ' . mysqli_error($conn);
}


$sql_jobs = 'SELECT * FROM jobs';
$result_jobs = mysqli_query($conn, $sql_jobs);

if ($result_jobs) {
    echo '<h2>Job Information</h2>';
    echo '<table border="1">';
    echo '<tr><th>ID</th><th>Title</th><th>Company</th><th>Location</th></tr>';

    while ($row = mysqli_fetch_assoc($result_jobs)) {
        echo '<tr>';
        echo '<td>' . $row['id'] . '</td>';
        echo '<td>' . $row['title'] . '</td>';
        echo '<td>' . $row['company'] . '</td>';
        echo '<td>' . $row['location'] . '</td>';
        echo '</tr>';
    }

    echo '</table>';
} else {
    echo 'Error fetching job information: ' . mysqli_error($conn);
}

mysqli_close($conn);
ob_end_flush();

?>


<!DOCTYPE html>
<html>
<head>
    <title>User Information</title>
</head>
<body>
    <h1>Information</h1>
</body>
</html>
