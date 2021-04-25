from svgpathtools import parse_path, wsvg, svg2paths
from functools import reduce
import math
from shapely.geometry import box

def similarPaths(path1, path2):
    for a in list(path1) + list(path2):
        if a.start == a.end:
            return False
        
    threshold = 1
    steps = 100
    try:
        tangents1 = [path1.unit_tangent(float(t) / float(steps)) for t in range(0, steps)]
        tangents2 = [path2.unit_tangent(float(t) / float(steps)) for t in range(0, steps)]
    except AssertionError:
        return False

    tansub1 = []
    tansub2 = []

    for i in range(0, steps - 1):
        tansub1.append(tangents1[i] - tangents1[i+1])
        tansub2.append(tangents2[i] - tangents2[i+1])

    differences = list(map(lambda pair: abs(pair[0]-pair[1]), zip(tansub1, tansub2)))
    differences.sort()

    diff = reduce(lambda x, y:x+y, differences)

    return diff < threshold

def diffSvgs(originalPaths, searchPaths):
    pathCount = len(originalPaths)
    for angel in range(0, 7):
        matched = False
        matchCount = 0
        for pathConfig in originalPaths:
            path = pathConfig.rotated(45 * angel)

            matched = any(similarPaths(path, checkPath) for checkPath in searchPaths)

            if matched:
                matchCount += 1

        print(pathCount, matchCount)
        if float(matchCount) / float(pathCount) > 0.95:
            return True
    
    return False

def intersectBoxes(svg_bbox, test_box):
    svg_box = box(svg_bbox[0], svg_bbox[1], svg_bbox[2], svg_bbox[3])
    return svg_box.intersects(test_box)

def filterBoxedPathsFromSvg(svg, test_box):
    return filter(lambda path: intersectBoxes(path.bbox(), test_box), svg)

test_svg = svg2paths('./example/orig.svg')[0]
match_svg = svg2paths('./example/match.svg')[0]
random_svg = svg2paths('./example/random.svg')[0]

print(diffSvgs(test_svg, match_svg))
print(diffSvgs(test_svg, random_svg))