pcall(load(S4.arg))

-- period = 1000/600
-- subp = 500
-- gratingthickness = 750
-- dutycycle = 0.5
-- ridgewidth = subp * dutycycle
-- gratingindex = 2
-- sio2index = 1.45
-- loss = 0.0

-- nharm = 20
-- TEamp = 0
-- TMamp = 1

-- zmin = -500
-- zmax = 660
-- xmin = -750
-- xmax = 750

-- lambda1 =  750 --803.33333 -- 727

  local filespectrum = io.open("spectrum_E.csv","w")
  local fileeps = io.open("eps_r.csv","w")
    
      S = S4.NewSimulation()
      S:SetLattice(period)
      S:SetNumG(nharm)
      S:UsePolarizationDecomposition()

      S:AddMaterial("GratingMaterial", {gratingindex^2,0})
      S:AddMaterial("Air", {1,0})
      S:AddMaterial("SiO2", {sio2index^2,0})

      S:AddLayer('AirAbove', 0, 'Air')
      S:AddLayer('Grating', gratingthickness, 'Air') -- Air inbetween
      S:SetLayerPatternRectangle('Grating', 'GratingMaterial', {0,0}, 0, {ridgewidth*0.5,0})
      S:AddLayer('SiDioxide', 0, 'SiO2')

      -- S:AddLayer('AirAbove', 0, 'Air')

      -- S:AddLayer('Grating', gratingthickness, 'Air') -- Air inbetween

      -- S:SetLayerPatternRectangle('Grating', 'GratingMaterial', {225,0}, 0, {ridgewidth*0.5,0}) -- ITO grating - layer, material in rectangle, centre, tilt-angle, half-widths
      -- S:SetLayerPatternRectangle('Grating', 'GratingMaterial', {-225,0}, 0, {ridgewidth*0.5,0})

      -- S:SetLayerPatternRectangle('Grating', 'AccumLayer', {380,0}, 0, {accum_width*0.5,0})
      -- S:SetLayerPatternRectangle('Grating', 'AccumLayer', {70,0}, 0, {accum_width*0.5,0})
      -- S:SetLayerPatternRectangle('Grating', 'DepLayer', {-70,0}, 0, {accum_width*0.5,0})
      -- S:SetLayerPatternRectangle('Grating', 'DepLayer', {-380,0}, 0, {accum_width*0.5,0})

      -- S:AddLayer('SiDioxide', 0, 'SiO2')

      S:SetExcitationPlanewave({0,0},      -- incidence angles (spherical coords: phi [0,180], theta [0,360])
                         {TEamp,0},  -- TE-polarisation amplitude and phase (in degrees)
                         {TMamp,0})  -- TM-polarisation amplitude and phase
    
     -- COMPUTE AND SAVE TRANSMISSION / REFLECTION
	         freq = 1/lambda1
	         S:SetFrequency(freq)
	          inc, back = S:GetPowerFlux('AirAbove', 20)
	          refl = - back/inc

              for z = zmin, zmax, zstep do
                lat = ''
                eps = ''
                for x = xmin, xmax, xstep do
                 Exr, Eyr, Ezr, Exi, Eyi, Ezi = S:GetEField({0,x,z})
                 lat = lat..(Eyr^2)..','

                 eps_r, eps_i = S:GetEpsilon({x, 0, z})
                 eps = eps..eps_r..','
                 
                end
                lat = string.sub(lat, 1, -2)
                lat = lat..'\n'
                eps = string.sub(eps, 1, -2)
                eps = eps..'\n'

        filespectrum:write(lat) 
        fileeps:write(eps) 
        print('z=', z) 
    end 

    filespectrum:close()

