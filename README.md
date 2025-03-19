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

## Implentation

This section includes my implentation method and the results.

### Method

I used one script to process the data then map trees and roads. The other is for the correlation process. 

The interactive map is provided as an html provided which can be opened in your browser. This was done to provide a visual method of finding tree to speed correlation. Each road marker has some information on the speed of that road.

<b>Challenges:</b>

1. The road speed limit data has the roads as line geometry. To solve this I found the centroid point of the line segments to use as a marker for the map. *Most curved roads would cause the centroid to be off the road. 

2. The trees include data from 1955 to 2024. As a naive remedy, I removed all the trees planted after 2008 since those trees wouldn't be mature or existent.

### Results

Screenshots from the correlation process are included in the screenshots folder. The map was an semi-efficient interactive tool to discover and correlations. At first I thought to notice some correlations but then I looked at the road on Google Maps 3D and saw that it might be to the road features as I kind of thought. Then, the correlation heat map along with the scatter plot showed there there is little to <b>no</b> correlation with people speeding to the nearby trees along the road. I partially expected this, but also thought there might be at least a lot. The correlation with the speed data to the nearby trees averaged -0.115, or little to no correlation as the value is closer to 0.

The Clement Street picture truly shoes that trees have no correlation to slowing people down! 83% drove over the limit but there are a lot of trees.

## Conclusion

Overall this was an interesting task to work on and was interesting to me that most of the process is working on the data before doing any analyzing.

