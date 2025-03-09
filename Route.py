class Route:
    def __init__(self, stations: list, distances : list):
        self.__stations = stations
        self.__distances = distances

    @property
    def get_stations(self):
        return self.__stations 
    
    @property 
    def get_distances(self):
        return self.__distances

    def calculate_distance(self, source: str, destination: str):
        source_index = self.__stations.index(source)
        destination_index = self.__stations.index(destination)
        return sum(self.__distances[source_index:destination_index])