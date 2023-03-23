-- pcall(load(S4.arg))

period = 1332
subp = 666
gratingthickness = 500
dutycycle = 494/666
ridgewidth = subp * dutycycle
gratingindex = 3.3
sio2index = 1.5 

nharm = 20
lambdain = 1400
lambdafin = 1700
npoints = 900 --900

TEamp = 1
TMamp = 0

deltalambda = (lambdafin - lambdain) / npoints

theta_min = 1
theta_max = 15

deltalambda = (lambdafin - lambdain) / npoints

local filespectrum = io.open("spectrum.csv","w")
    
      S = S4.NewSimulation()
      S:SetLattice(period)
      S:SetNumG(nharm)
      S:UsePolarizationDecomposition()

      S:AddMaterial("GratingMaterial", {gratingindex^2,0})
      S:AddMaterial("Air", {1,0})
      S:AddMaterial("SiO2", {sio2index^2,0})
      
      S:AddLayer('AirAbove', 0, 'Air')
      
      S:AddLayer('Grating', gratingthickness, 'Air') -- Air inbetween
      
      S:SetLayerPatternRectangle('Grating', 'GratingMaterial', {319,0}, 0, {ridgewidth*0.5,0}) -- ITO grating - layer, material in rectangle, centre, tilt-angle, half-widths
      S:SetLayerPatternRectangle('Grating', 'GratingMaterial', {-319,0}, 0, {ridgewidth*0.5,0})
      
      S:AddLayer('AirMid', 300, 'Air')
      
      S:AddLayer('SiDioxide', 0, 'SiO2')

      for theta = theta_min, theta_max, 1 do
            lat = ''
            for lambda = lambdain, lambdafin, deltalambda do
                    S:SetExcitationPlanewave({theta,0},   -- incidence angles (spherical coords: phi [0,180], theta [0,360])
                                            {TEamp,0},  -- TE-polarisation amplitude and phase (in degrees)
                                            {TMamp,0})  -- TM-polarisation amplitude and phase
                    
                    freq = 1/lambda
                    S:SetFrequency(freq)
                    inc, back = S:GetPowerFlux('AirAbove', 20)
                    forward, backward = S:GetPowerFlux('SiDioxide', 20)
                    refl = - back/inc

                    lat = lat..refl..','
            end
                    lat = string.sub(lat, 1, -2)
                    lat = lat..'\n'

                    filespectrum:write(lat) 
                    print('θ=', theta, 'λ=', lambda) 
            end
        end 



    filespectrum:close()

