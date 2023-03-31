%define oname Nevoso
%define bdate   2019.01.18

Summary:    Nevoso Plasma 5 Aurorae theme for OpenMandriva
Name:   	openmandriva-nevoso
Version:    1
Release:    3
License:    GPL
Group:  Graphical desktop/KDE
Url:    https://www.opendesktop.org/u/caig/
Source0:    %{oname}%{bdate}.tar.gz
# Source backup available here: https://github.com/AngryPenguinPL/Nevoso

BuildRequires:	extra-cmake-modules
BuildArch:	noarch

%description
Nevoso Plasma 5 Aurorae theme for OpenMandriva Linux created by caig

%files
%dir %{_kde5_datadir}/aurorae/themes/Nevoso/
%{_kde5_datadir}/aurorae/themes/Nevoso/*

#----------------------------------------------------------------------------

%prep
%setup -qn %{oname}

%build

%install
mkdir -p %{buildroot}%{_kde5_datadir}/aurorae/themes/Nevoso
cp * %{buildroot}%{_kde5_datadir}/aurorae/themes/Nevoso/
