from usecases.image import calc_image_similarity


class LandmarkService:
    @staticmethod
    async def ImageCompare(image_request):
        similarity = calc_image_similarity(
            image_request.img, image_request.landmark_id)
        threshold = 0.5
        # similarityは、一致度が高いほど0に近くなるため
        if similarity < threshold:
            return "OK"
        return "NG"
