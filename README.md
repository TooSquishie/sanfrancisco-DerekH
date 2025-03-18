# San Francisco - Derek Hodgkins.
Data Mining course project based on the data sets from https://data.sfgov.org/ 

## Task

### Problem

**What can I do to help San Francisco?**

*Analyze the affect of street trees on speed limit compliance!*

It's no mystery that drivers drive over the posted speed limit more often than not. However, some measures can be taken to reduce this behavior apart from speed bumps, traffic circles, etc. As seen in this [article about road design tricks](https://www.bbc.com/future/article/20140417-road-designs-that-trick-our-minds), certain road designs can cause drivers to drive slower or faster. My question is this: do street-side trees have that same affect? Do drivers go slower or faster? Maybe it has no effect. My implentation will see if a correlation exists.

### Solution

To complete this task, I will look at street trees that are around speeding hot spots. Then, I will see what effects trees may cause by looking visually at a graph and finding numerical correlation score.

### Challenges

1. There are many other variable that would effect drivers' speed limit compliance such as pedestrians, road design (as seen in article), land features, etc.

2. The SF Speed Limit Compliance data has a feature called 'thegeom' which is collection of points in the form (Longitute, Latitude). My plan is use to the center of points as the effect location to maintain simplicity.

3. There are almost 200,000 trees from 1955 to 2024. I will use only the trees planted before 2008 for a semi-realistic approach since trees planted after that wouldn't be visible from 2004-2009. Additionally, I will only use trees that are near the roads in the Speed Limit Compliance dataset since trees far away wouldnt be be important.

## Data

The following section includes the 2 datasets that I will be using for my task.

### SF Street Tree List

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

### SF Speed Limit Compliance

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