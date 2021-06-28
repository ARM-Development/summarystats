from numpy.testing import assert_almost_equal
import pyart
import summarystats.coveragearea

def test_rain_coverage():
    test_radar = pyart.io.read('../tests/data/corcsapr2cmacppiM1.c1.20181012.001503.nc')

    test_rain = summarystats.coveragearea.rain_coverage(test_radar)

    assert_almost_equal(test_rain, 11.29287, decimal=5)

def test_snow_coverage():
    test_radar = pyart.io.read('../tests/data/corcsapr2cmacppiM1.c1.20181012.001503.nc')

    test_snow = summarystats.coveragearea.snow_coverage(test_radar)

    assert_almost_equal(test_snow, 4.56257, decimal=5)

def test_convection_coverage():
    test_radar = pyart.io.read('../tests/data/corcsapr2cmacppiM1.c1.20181012.001503.nc')

    test_conv = summarystats.coveragearea.convection_coverage(test_radar)

    assert_almost_equal(test_conv, 0.05112, decimal=5)