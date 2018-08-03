<?php

$servername = "localhost";
$username = "root";
$password = "";
$db = "loja";

$conn = new mysqli($servername, $username, $password, $db);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 
$sql = "SELECT email, nome FROM usuario";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo "<tr><td>" . $row["email"]. "</td><td>" . $row["nome"]. "</td></<tr>";
    }
} else {
    echo "0 results";
}
$conn->close();
?>