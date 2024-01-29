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

mysqli_close($conn);
?>


<!DOCTYPE html>
<html>
<head>
    <title>User Information</title>
</head>
<body>
    <h1>User Information</h1>
</body>
</html>
