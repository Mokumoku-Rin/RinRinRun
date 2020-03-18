function deg2rad(deg){
  return deg * ( Math.PI / 180 )
}

const GpsUtil = {
  install (Vue) {
      Vue.prototype.$calDistance = (positionList) => {
        let distance = 0.0
      
        if(positionList.length < 2)return 0
      
        for(let i=1; i<positionList.length; i++){
          // 緯度経度をラジアンに変換
          const radLatitudeA = deg2rad(positionList[i-1][0])
          const radLongitudeA = deg2rad(positionList[i-1][1])
          const radLatitudeB = deg2rad(positionList[i][0])
          const radLongitudeB = deg2rad(positionList[i][1])
      
          const radLatDiff = radLatitudeA - radLatitudeB
          const radLonDiff = radLongitudeA - radLongitudeB
      
          const radLatAve = (radLatitudeA + radLatitudeB) / 2.0;
      
          const a = 6378137.0 // 赤道半径
          const e2 = 0.00669438002301188 // 第一離心率^2
          const a1e2 = 6335439.32708317 // 赤道上の子午線曲率半径
      
          let sinLat = Math.sin(radLatAve)
      
          sinLat = Math.sin(radLatAve)
          let W2 = 1.0 - e2 * (sinLat*sinLat)
          let M = a1e2 / (Math.sqrt(W2)*W2); // 子午線曲率半径M
          let N = a / Math.sqrt(W2); // 卯酉線曲率半径
      
          let t1 = M * radLatDiff
          let t2 = N * Math.cos(radLatAve) * radLonDiff
          let dist = Math.sqrt((t1*t1) + (t2*t2))
      
          distance += dist
        }
        return distance
      }
        
  }
}
    
export default GpsUtil