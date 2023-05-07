-- script that lists all bands with Glam rock as their main style
SELECT band_name AS band_name, split - formed AS lifespan FROM metal_bands
WHERE style='Glam rock'
GROUP BY band_name ORDER BY lifespan DESC;
