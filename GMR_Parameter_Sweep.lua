pcall(load(S4.arg))

local filespectrum = io.open("Refl_data.csv","w")

S = S4.NewSimulation()
S:SetLattice(p)
S:SetNumG(nharm)
S:UsePolarizationDecomposition()

S:AddMaterial("GratingMaterial", {n^2,0})
S:AddMaterial("Air", {1,0})
S:AddMaterial("Water", {1.331,0})
S:AddMaterial("substrate", {subindex^2,0})

S:AddLayer('AirAbove', 0, 'Water')
S:AddLayer('Grating', gratingthickness, 'Air') -- Air inbetween
S:SetLayerPatternRectangle('Grating', 'GratingMaterial', {0,0}, 0, {p * dutycycle * 0.5,0})
S:AddLayer('Substrate', 0, 'substrate')

S:SetExcitationPlanewave({0,0},      -- incidence angles (spherical coords: phi [0,180], theta [0,360])
                         {TEamp,0},  -- TE-polarisation amplitude and phase (in degrees)
                         {TMamp,0})  -- TM-polarisation amplitude and phase
   
freq = 1/lambda1
S:SetFrequency(freq)
inc, back = S:GetPowerFlux('AirAbove', 0)
forward, backward = S:GetPowerFlux('Substrate', 20)
refl = - back/inc

filespectrum:write("\n", refl)
filespectrum:close()