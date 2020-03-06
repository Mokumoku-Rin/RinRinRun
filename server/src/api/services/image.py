from usecases.image import compare_image


class ImageService:
    @staticmethod
    async def ImageCompare(image_request):
        similarity = compare_image(
            image_request.img, image_request.landmark_id)
        threshold = 0.5
        # similarityは、一致度が高いほど0に近くなるため
        if similarity < threshold:
            return "OK"
        return "NG"
