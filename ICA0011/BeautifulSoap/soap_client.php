<?php

error_reporting(E_ALL);
ini_set('display_errors', 'On');
header('Content-Type: application/json');

$client = new SoapClient('http://localhost:8000/?wsdl');

$disk = $client->disk_usage();
$dns = $client->dns_records(array('name' => 'google.com'));
$user_info = $client->get_information(array('reachable_host' => 'google.com'));

echo json_encode([$user_info, $dns, $disk], JSON_PRETTY_PRINT);

?>