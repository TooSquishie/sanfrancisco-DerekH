# San Francisco.
Data Mining course project based on the data sets from https://data.sfgov.org/ 

# Data

## SF Street Tree List

List of maintained street trees since 1955.

[SF OpenData Street Tree List](https://data.sfgov.org/City-Infrastructure/Street-Tree-List/tkzw-k3nq/about_data)

198k Rows
18 Columns

Each row is a stree tree.

<table border="0">
 <tr>
    <td><b style="font-size:30px">Column Name</b></td>
    <td><b style="font-size:30px">Data Type</b></td>
 </tr>
 <tr>
    <td>TreeID</td>
    <td>Number</td>
 </tr>
 <tr>
    <td>qLegalStatus</td>
    <td>Text</td>
 </tr>
 <tr>
    <td>qSpecies</td>
    <td>Text</td>
 </tr>
 <tr>
    <td>qAddress</td>
    <td>Text</td>
 </tr>
 <tr>
    <td>SiteOrder</td>
    <td>Number</td>
 </tr>
 <tr>
    <td>qSiteInfo</td>
    <td>Text</td>
 </tr>
 <tr>
    <td>Plant Type</td>
    <td>Text</td>
 </tr>
 <tr>
    <td>qCaretaker</td>
    <td>Text</td>
 </tr>
 <tr>
    <td>qCareAssistant</td>
    <td>Text</td>
 </tr>
 <tr>
    <td>PlantDate</td>
    <td>Floating Timestamp</td>
 </tr>
 <tr>
    <td>DBH</td>
    <td>Number</td>
 </tr>
 <tr>
    <td>PlotSize</td>
    <td>Text</td>
 </tr>
 <tr>
    <td>PermitNotes</td>
    <td>Text</td>
 </tr>
 <tr>
    <td>XCoord</td>
    <td>Number</td>
 </tr>
 <tr>
    <td>YCoord</td>
    <td>Number</td>
 </tr>
 <tr>
    <td>Latitude</td>
    <td>Number</td>
 </tr>
 <tr>
    <td>Longitude</td>
    <td>Number</td>
 </tr>
 <tr>
    <td>Location</td>
    <td>Location</td>
 </tr>
</table>

## SF Speed Limit Compliance

Statistics on speeding rates and exceedance of speed limit along selected street segments throughout San Francisco from 2004 - 2009.

[SF OpenData SPeed Limit Compliance Data](https://data.sfgov.org/Public-Safety/San-Francisco-Speed-Limit-Compliance/wytw-dqq4/about_data)

613 Rows
9 Columns

Each row is a segment of a road with speed limit compliance data.

<table border="0">
 <tr>
    <td><b style="font-size:30px">Column Name</b></td>
    <td><b style="font-size:30px">Data Type</b></td>
 </tr>
 <tr>
    <td>CNN</td>
    <td>Number</td>
 </tr>
  <tr>
    <td>the_geom</td>
    <td>Line</td>
 </tr>
  <tr>
    <td>SpeedLimit</td>
    <td>Number</td>
 </tr>
  <tr>
    <td>STREETNAME</td>
    <td>Text</td>
 </tr>
  <tr>
    <td>Over_pct</td>
    <td>Number</td>
 </tr>
  <tr>
    <td>O5mph_pct</td>
    <td>Number</td>
 </tr>
  <tr>
    <td>Speed_avg</td>
    <td>Number</td>
 </tr>
  <tr>
    <td>SpeedO_avg</td>
    <td>Number</td>
 </tr>
  <tr>
    <td>Spd5O_avg</td>
    <td>Number</td>
 </tr>
</table>