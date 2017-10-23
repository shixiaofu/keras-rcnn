import keras.backend
import keras.utils
import numpy

import keras_rcnn.layers
import keras_rcnn.layers.object_detection._proposal_target as proposal_target


class TestProposalTarget:
    def test_call(self):
        proposal_target = keras_rcnn.layers.ProposalTarget()

        proposals = numpy.random.random((1, 300, 4))
        proposals = keras.backend.variable(proposals)

        bounding_boxes = numpy.random.choice(range(0, 224), (1, 10, 4))
        bounding_boxes = keras.backend.variable(bounding_boxes)

        labels = numpy.random.choice(range(0, 2), (1, 10))
        labels = keras.utils.to_categorical(labels)
        labels = keras.backend.variable(labels)
        labels = keras.backend.expand_dims(labels, 0)

        proposal_target.call([proposals, labels, bounding_boxes])

    def test_build(self):
        pass

    def test_compute_output_shape(self):
        pass

    def test_compute_mask(self):
        pass

    def test_set_label_background(self):
        pass

    def test_get_bbox_targets(self):
        pass

    def test_get_fg_bg_rois(self):
        pass

    def test_sample_indices(self):
        pass

    def test_sample_rois(self):
        n = 5
        gt_boxes = numpy.zeros((n, 4))
        gt_boxes = keras.backend.variable(gt_boxes)
        num_classes = 3
        gt_labels = numpy.reshape(
            [[0, 1, 0], [1, 0, 0], [1, 0, 0], [0, 0, 1], [0, 1, 0]], (-1, 3))
        gt_labels = keras.backend.variable(gt_labels)

        fg_thresh = 0.7
        fg_fraction = 0.5
        batchsize = 256
        num_images = 1
        n_proposals = 200
        all_rois = keras.backend.zeros((n_proposals, 4))

        rois_per_image = batchsize // num_images
        fg_rois_per_image = int(fg_fraction * rois_per_image)
        proposal_target = keras_rcnn.layers.ProposalTarget()
        rois, labels, bbox_targets = proposal_target.sample_rois(
            all_rois, gt_boxes, gt_labels)
        assert keras.backend.eval(labels).shape == (n_proposals, num_classes)
        assert keras.backend.eval(rois).shape == (n_proposals, 4)

        y = (n_proposals, 4 * num_classes)
        assert keras.backend.eval(bbox_targets).shape == y

        all_rois = numpy.array([
        [ 147.76878357,   29.01632309,  223.        ,  114.99934387],
        [ 147.        ,   25.        ,  222.        ,  111.        ],
        [   0.        ,    0.        ,  209.16778564,   68.49925232],
        [   0.        ,    0.        ,  211.00296021,  162.87817383],
        [  32.66508484,    4.43878937,  223.        ,  186.33660889],
        [  95.74607849,    0.        ,  223.        ,  151.88378906],
        [  80.61355591,    0.        ,  210.17364502,  123.88359833],
        [ 172.40184021,   87.03622437,  223.        ,  144.41511536],
        [   0.        ,    0.        ,  223.        ,   47.3677063 ],
        [   0.        ,    0.        ,  221.79241943,  223.        ],
        [  21.99452209,    0.        ,  223.        ,  101.71372986],
        [ 132.54067993,    0.        ,  223.        ,  158.1519165 ],
        [  81.24060822,    1.23635864,  195.14959717,  223.        ],
        [ 103.69470215,   45.542099  ,  213.39746094,  223.        ],
        [ 159.75787354,    0.        ,  210.78341675,  223.        ],
        [  94.54430389,    0.        ,  183.53781128,  127.90118408],
        [ 153.93727112,   49.92974854,  223.        ,  210.13116455],
        [ 130.90890503,   18.70446777,  223.        ,  221.6697998 ],
        [  85.27020264,    0.        ,  223.        ,   62.93292999],
        [  97.63447571,   12.87449646,  223.        ,  119.77130127],
        [ 149.14425659,   65.97438049,  223.        ,  149.6988678 ],
        [  45.83560181,    0.        ,  223.        ,   79.00631714],
        [ 169.77224731,   58.25152588,  223.        ,  188.60289001],
        [  86.21421051,   34.39504242,  223.        ,  146.52676392],
        [  99.97828674,    6.92190552,  223.        ,  207.4954834 ],
        [ 171.24017334,    3.87971497,  223.        ,   95.53321075],
        [ 112.39691162,   58.04541779,  223.        ,  162.69979858],
        [  79.37534332,   80.01358795,  223.        ,  135.39920044],
        [  60.60487366,   73.39674377,  212.87239075,  144.02378845],
        [ 123.95248413,   38.94178009,  223.        ,  153.16690063],
        [  67.47679901,   25.079216  ,  205.42700195,  101.39093781],
        [  54.00462341,   48.15732574,  223.        ,  169.70031738],
        [  56.85334015,   16.12230682,  223.        ,  223.        ],
        [ 150.11177063,    0.        ,  223.        ,   75.33294678],
        [ 127.90908051,    0.        ,  223.        ,   64.03712463],
        [ 162.10505676,   70.14424133,  223.        ,  117.29508972],
        [   2.18456268,   23.49804306,  184.81402588,   76.63926697],
        [ 173.13052368,    0.        ,  223.        ,  223.        ],
        [  76.91851807,    0.        ,  194.33621216,   68.61004639],
        [ 173.81614685,   49.29305267,  223.        ,  139.01824951],
        [  87.84130859,   71.30104065,  223.        ,  152.91740417],
        [  80.61021423,    0.        ,  169.43260193,  119.19921875],
        [ 113.13809204,    0.        ,  200.85342407,  112.93939209],
        [  76.85679626,   56.87866211,  223.        ,  126.87872314],
        [ 148.33416748,    0.        ,  198.74414062,  223.        ],
        [ 160.85856628,   74.05710602,  223.        ,  159.27407837],
        [  24.3434906 ,   44.09479141,  216.30944824,   97.67276001],
        [   0.        ,   19.5617218 ,  223.        ,   92.74246979]], dtype=numpy.float32)

        gt_boxes = numpy.array([[ 147.,   25.,  222.,  111.]])

        rois, labels, bbox_targets = proposal_target.sample_rois(
            all_rois, gt_boxes, gt_labels)

        expected_rois = numpy.array([[ 147.        ,   25.        ,  222.        ,  111.        ],
        [ 147.76878357,   29.01632309,  223.        ,  114.99934387],
        [  85.27020264,    0.        ,  223.        ,   62.93292999],
        [ 148.33416748,    0.        ,  198.74414062,  223.        ],
        [ 162.10505676,   70.14424133,  223.        ,  117.29508972],
        [  45.83560181,    0.        ,  223.        ,   79.00631714],
        [ 150.11177063,    0.        ,  223.        ,   75.33294678],
        [ 160.85856628,   74.05710602,  223.        ,  159.27407837],
        [   0.        ,    0.        ,  211.00296021,  162.87817383],
        [  32.66508484,    4.43878937,  223.        ,  186.33660889],
        [   0.        ,    0.        ,  221.79241943,  223.        ],
        [  86.21421051,   34.39504242,  223.        ,  146.52676392],
        [   0.        ,    0.        ,  209.16778564,   68.49925232],
        [  24.3434906 ,   44.09479141,  216.30944824,   97.67276001],
        [ 113.13809204,    0.        ,  200.85342407,  112.93939209],
        [ 173.81614685,   49.29305267,  223.        ,  139.01824951],
        [  60.60487366,   73.39674377,  212.87239075,  144.02378845],
        [  79.37534332,   80.01358795,  223.        ,  135.39920044],
        [  54.00462341,   48.15732574,  223.        ,  169.70031738],
        [  80.61355591,    0.        ,  210.17364502,  123.88359833],
        [ 132.54067993,    0.        ,  223.        ,  158.1519165 ],
        [  99.97828674,    6.92190552,  223.        ,  207.4954834 ],
        [  87.84130859,   71.30104065,  223.        ,  152.91740417],
        [  80.61021423,    0.        ,  169.43260193,  119.19921875],
        [  76.85679626,   56.87866211,  223.        ,  126.87872314],
        [ 159.75787354,    0.        ,  210.78341675,  223.        ],
        [ 112.39691162,   58.04541779,  223.        ,  162.69979858],
        [  97.63447571,   12.87449646,  223.        ,  119.77130127],
        [  21.99452209,    0.        ,  223.        ,  101.71372986],
        [ 153.93727112,   49.92974854,  223.        ,  210.13116455],
        [  94.54430389,    0.        ,  183.53781128,  127.90118408],
        [ 169.77224731,   58.25152588,  223.        ,  188.60289001],
        [  76.91851807,    0.        ,  194.33621216,   68.61004639],
        [   0.        ,    0.        ,  223.        ,   47.3677063 ],
        [  67.47679901,   25.079216  ,  205.42700195,  101.39093781],
        [ 123.95248413,   38.94178009,  223.        ,  153.16690063],
        [   2.18456268,   23.49804306,  184.81402588,   76.63926697],
        [ 103.69470215,   45.542099  ,  213.39746094,  223.        ],
        [  81.24060822,    1.23635864,  195.14959717,  223.        ],
        [ 171.24017334,    3.87971497,  223.        ,   95.53321075],
        [  95.74607849,    0.        ,  223.        ,  151.88378906],
        [  56.85334015,   16.12230682,  223.        ,  223.        ],
        [ 149.14425659,   65.97438049,  223.        ,  149.6988678 ],
        [ 130.90890503,   18.70446777,  223.        ,  221.6697998 ],
        [ 127.90908051,    0.        ,  223.        ,   64.03712463],
        [ 173.13052368,    0.        ,  223.        ,  223.        ],
        [ 172.40184021,   87.03622437,  223.        ,  144.41511536],
        [   0.        ,   19.5617218 ,  223.        ,   92.74246979]])
        numpy.testing.assert_almost_equal(keras.backend.eval(rois).sum(), expected_rois.sum(), 2)

        expected_labels = numpy.array([ 1.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
         0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
         0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
         0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.])
        numpy.testing.assert_almost_equal(keras.backend.eval(labels)[:, 1].sum(), expected_labels.sum(), 2)

        expected_boxes = numpy.array([[0., 0., 0., 0., 0.,
                                       0., 0., 0.],
                                      [0., 0., 0., 0., -0.01160154,
                                       -0.04607598, -0.0030377, 0.00019523],
                                      [0., 0., 0., 0., 0.,
                                       0., 0., 0.],
                                      [0., 0., 0., 0., 0.,
                                       0., 0., 0.],
                                      [0., 0., 0., 0., 0.,
                                       0., 0., 0.],
                                      [0., 0., 0., 0., 0.,
                                       0., 0., 0.],
                                      [0., 0., 0., 0., 0.,
                                       0., 0., 0.],
                                      [0., 0., 0., 0., 0.,
                                       0., 0., 0.],
                                      [0., 0., 0., 0., 0.,
                                       0., 0., 0.],
                                      [0., 0., 0., 0., 0.,
                                       0., 0., 0.],
                                      [0., 0., 0., 0., 0.,
                                       0., 0., 0.],
                                      [0., 0., 0., 0., 0.,
                                       0., 0., 0.],
                                      [0., 0., 0., 0., 0.,
                                       0., 0., 0.],
                                      [0., 0., 0., 0., 0.,
                                       0., 0., 0.],
                                      [0., 0., 0., 0., 0.,
                                       0., 0., 0.],
                                      [0., 0., 0., 0., 0.,
                                       0., 0., 0.],
                                      [0., 0., 0., 0., 0.,
                                       0., 0., 0.],
                                      [0., 0., 0., 0., 0.,
                                       0., 0., 0.],
                                      [0., 0., 0., 0., 0.,
                                       0., 0., 0.],
                                      [0., 0., 0., 0., 0.,
                                       0., 0., 0.],
                                      [0., 0., 0., 0., 0.,
                                       0., 0., 0.],
                                      [0., 0., 0., 0., 0.,
                                       0., 0., 0.],
                                      [0., 0., 0., 0., 0.,
                                       0., 0., 0.],
                                      [0., 0., 0., 0., 0.,
                                       0., 0., 0.],
                                      [0., 0., 0., 0., 0.,
                                       0., 0., 0.],
                                      [0., 0., 0., 0., 0.,
                                       0., 0., 0.],
                                      [0., 0., 0., 0., 0.,
                                       0., 0., 0.],
                                      [0., 0., 0., 0., 0.,
                                       0., 0., 0.],
                                      [0., 0., 0., 0., 0.,
                                       0., 0., 0.],
                                      [0., 0., 0., 0., 0.,
                                       0., 0., 0.],
                                      [0., 0., 0., 0., 0.,
                                       0., 0., 0.],
                                      [0., 0., 0., 0., 0.,
                                       0., 0., 0.],
                                      [0., 0., 0., 0., 0.,
                                       0., 0., 0.],
                                      [0., 0., 0., 0., 0.,
                                       0., 0., 0.],
                                      [0., 0., 0., 0., 0.,
                                       0., 0., 0.],
                                      [0., 0., 0., 0., 0.,
                                       0., 0., 0.],
                                      [0., 0., 0., 0., 0.,
                                       0., 0., 0.],
                                      [0., 0., 0., 0., 0.,
                                       0., 0., 0.],
                                      [0., 0., 0., 0., 0.,
                                       0., 0., 0.],
                                      [0., 0., 0., 0., 0.,
                                       0., 0., 0.],
                                      [0., 0., 0., 0., 0.,
                                       0., 0., 0.],
                                      [0., 0., 0., 0., 0.,
                                       0., 0., 0.],
                                      [0., 0., 0., 0., 0.,
                                       0., 0., 0.],
                                      [0., 0., 0., 0., 0.,
                                       0., 0., 0.],
                                      [0., 0., 0., 0., 0.,
                                       0., 0., 0.],
                                      [0., 0., 0., 0., 0.,
                                       0., 0., 0.],
                                      [0., 0., 0., 0., 0.,
                                       0., 0., 0.],
                                      [0., 0., 0., 0., 0.,
                                       0., 0., 0.]])
        numpy.testing.assert_almost_equal(keras.backend.eval(bbox_targets).sum(), expected_boxes.sum(), 2)




def test_get_bbox_regression_labels():
    n = 10
    bbox_target_data = keras.backend.zeros((n, 4))
    num_classes = 3
    labels = numpy.reshape(
        [[0, 1, 0], [1, 0, 0], [1, 0, 0], [0, 0, 1], [0, 1, 0]], (1, -1, 3))
    labels = keras.backend.variable(labels)
    bbox_targets = proposal_target.get_bbox_regression_labels(
        labels, bbox_target_data)
    bbox_targets = keras.backend.eval(bbox_targets)

    assert bbox_targets.shape == (n, 4 * num_classes)



