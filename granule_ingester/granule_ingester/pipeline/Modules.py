from granule_ingester.processors import (GenerateTileId,
                                         TileSummarizingProcessor,
                                         EmptyTileFilter,
                                         KelvinToCelsius,
                                         Subtract180FromLongitude,
                                         ForceAscendingLatitude)
from granule_ingester.processors.reading_processors import (EccoReadingProcessor,
                                                            GridReadingProcessor,
                                                            SwathReadingProcessor,
                                                            TimeSeriesReadingProcessor)
from granule_ingester.slicers import SliceFileByStepSize
from granule_ingester.granule_loaders import GranuleLoader

modules = {
    "granule": GranuleLoader,
    "sliceFileByStepSize": SliceFileByStepSize,
    "generateTileId": GenerateTileId,
    "ECCO": EccoReadingProcessor,
    "Grid": GridReadingProcessor,
    "TimeSeries": TimeSeriesReadingProcessor,
    "Swath": SwathReadingProcessor,
    "tileSummary": TileSummarizingProcessor,
    "emptyTileFilter": EmptyTileFilter,
    "kelvinToCelsius": KelvinToCelsius,
    "subtract180FromLongitude": Subtract180FromLongitude,
    "forceAscendingLatitude": ForceAscendingLatitude
}
