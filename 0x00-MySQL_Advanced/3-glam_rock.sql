-- script that lists all bands with Glam rock as their main style
SELECT band_name AS band_name, IFNULL(split, 0) - IFNULL(formed, 0) AS lifespan 
FROM metal_bands
WHERE style='Glam rock'
GROUP BY band_name ORDER BY lifespan DESC;
