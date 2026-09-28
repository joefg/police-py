# police-py

`police-py` is a Python library providing a convenient interface for the
[data.police.uk](https://data.police.uk/) API. It allows you to easily fetch
real-time and historical data regarding UK police forces, crime statistics, and
officer activities.

## Features

The library provides specialized modules to interact with different types of data:

- **Crime Data**:
Retrieve detailed information about crimes, including street-level reports, outcomes, and no-location crimes.

- **Neighborhoods**:
Fetch information about police neighborhoods, including their boundaries, the teams assigned to them,
and their current priorities.

- **Police Forces**:
Access information about various police forces across the UK.

- **Stop and Search**:
Get data on stop and search activities across different regions and forces.

- **Availability**:
Check the availability of specific datasets.

## Installation

To install `police-py`, run the following command:

```bash
pip install .
```

It is also light enough to copy and paste into your project.

## Quick Start Examples

### Fetching Crime Data

Get street-level crime reports centered on a specific geographic coordinate:

```python
from police_py.crime import get_street_level_crimes_point

# Get crimes within one mile of a point in London
response = get_street_level_crimes_point(lat=51.5074, lng=-0.1278, date="2023-01")
print(response.json())
```

### Searching by Polygon

Get crime data within a custom defined polygon:

```python
from police_py.crime import get_street_level_crimes_poly

# Use a list of lat,lng pairs as a string: "lat,lng:lat,lng:..."
poly = "51.5074,-0.1278:51.51,-0.13:51.505,-0.12"
response = get_street_level_crimes_poly(poly, date="2023-01")
print(response.json())
```

### Getting Police Force Information

Get information about a specific police force:

```python
from police_py.forces import get_force

# Get information for the Metropolitan Police
response = get_force("met")
print(response.json())
```

### Retrieving Neighborhood Details

Find out about a specific neighborhood's boundaries and priorities:

```python
from police_py.neighbourhood import get_neighbourhood_bounds, get_neighbourhood_priorities

# Define the force and neighborhood ID
force = "met"
neighbourhood = "neighborhood_id_here"

# Get boundaries
bounds = get_neighbourhood_bounds(force, neighbourhood)
print(bounds.json())

# Get priorities
priorities = get_neighbourhood_priorities(force, neighbourhood)
print(priorities.json())
```

### Stop and Search Data

Get stop and search data for a specific force:

```python
from police_py.stop_and_search import get_stop_and_searches_by_force

# Get stop and search data for the Metropolitan Police for a specific month
response = get_stop_and_searches_by_force(force="met", date="2023-01")
print(response.json())
```

## Module Overview

- `police_py.crime`: Functions for fetching crime statistics, including those without a known location.
- `police_py.forces`: Access information about UK police forces and their personnel.
- `police_py.neighbourhood`: Details about geographic divisions, their teams, and actions.
- `police_py.stop_and_search`: Access official reports on "Stop and Search" police activity.
- `police_py.availability`: Check if specific data points are currently available.
